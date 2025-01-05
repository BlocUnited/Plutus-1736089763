from fastapi import HTTPException
from bson import ObjectId
from typing import List
from backend.models.portfolios import Portfolio

class PortfolioService:
    def __init__(self, db):
        self.db = db

    async def create_portfolio(self, portfolio: Portfolio):
        portfolio_dict = portfolio.dict()
        portfolio_dict['created_at'] = portfolio_dict['updated_at'] = str(datetime.utcnow())
        result = await self.db['Portfolios'].insert_one(portfolio_dict)
        return str(result.inserted_id)

    async def get_portfolio(self, portfolio_id: str):
        portfolio = await self.db['Portfolios'].find_one({'_id': ObjectId(portfolio_id)})
        if not portfolio:
            raise HTTPException(status_code=404, detail='Portfolio not found')
        return Portfolio.from_mongo(portfolio)

    async def update_portfolio(self, portfolio_id: str, portfolio_data: Portfolio):
        result = await self.db['Portfolios'].update_one({'_id': ObjectId(portfolio_id)}, {'$set': portfolio_data.dict(exclude_unset=True)})
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail='Portfolio not found or no changes made')
        return {'message': 'Portfolio updated successfully'}

    async def delete_portfolio(self, portfolio_id: str):
        result = await self.db['Portfolios'].delete_one({'_id': ObjectId(portfolio_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail='Portfolio not found')
        return {'message': 'Portfolio deleted successfully'}
