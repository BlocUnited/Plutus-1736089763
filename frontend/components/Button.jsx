import React from 'react';
import PropTypes from 'prop-types';
import './Button.css';

const Button = ({ label, type, disabled, onClick }) => {
    return (
        <button className={`btn btn-${type}`} disabled={disabled} onClick={onClick}>
            {label}
        </button>
    );
};

Button.propTypes = {
    label: PropTypes.string.isRequired,
    type: PropTypes.oneOf(['primary', 'secondary', 'danger']).isRequired,
    disabled: PropTypes.bool,
    onClick: PropTypes.func.isRequired,
};

Button.defaultProps = {
    disabled: false,
};

export default Button;
