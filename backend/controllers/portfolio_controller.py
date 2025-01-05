from fastapi import APIRouter, Depends, HTTPException
from backend.models.portfolios import Portfolio
from backend.services.portfolio_service import PortfolioService

router = APIRouter()

@router.post('/portfolios', response_model=str)
async def create_portfolio(portfolio: Portfolio, portfolio_service: PortfolioService = Depends()):
    return await portfolio_service.create_portfolio(portfolio)

@router.get('/portfolios/{portfolio_id}', response_model=Portfolio)
async def get_portfolio(portfolio_id: str, portfolio_service: PortfolioService = Depends()):
    return await portfolio_service.get_portfolio(portfolio_id)

@router.put('/portfolios/{portfolio_id}', response_model=dict)
async def update_portfolio(portfolio_id: str, portfolio: Portfolio, portfolio_service: PortfolioService = Depends()):
    return await portfolio_service.update_portfolio(portfolio_id, portfolio)

@router.delete('/portfolios/{portfolio_id}', response_model=dict)
async def delete_portfolio(portfolio_id: str, portfolio_service: PortfolioService = Depends()):
    return await portfolio_service.delete_portfolio(portfolio_id)
