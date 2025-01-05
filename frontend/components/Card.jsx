import React from 'react';
import PropTypes from 'prop-types';
import './Card.css';

const Card = ({ title, content, footer }) => {
    return (
        <div className="card">
            <h3>{title}</h3>
            <div>{content}</div>
            {footer && <div className="card-footer">{footer}</div>}
        </div>
    );
};

Card.propTypes = {
    title: PropTypes.string.isRequired,
    content: PropTypes.oneOfType([PropTypes.string, PropTypes.node]).isRequired,
    footer: PropTypes.oneOfType([PropTypes.string, PropTypes.node]),
};

export default Card;
