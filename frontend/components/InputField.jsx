import React from 'react';
import PropTypes from 'prop-types';
import './InputField.css';

const InputField = ({ type, placeholder, value, onChange }) => {
    return (
        <input
            type={type}
            placeholder={placeholder}
            value={value}
            onChange={onChange}
            className="input-field"
        />
    );
};

InputField.propTypes = {
    type: PropTypes.oneOf(['text', 'email', 'password']).isRequired,
    placeholder: PropTypes.string,
    value: PropTypes.string.isRequired,
    onChange: PropTypes.func.isRequired,
};

InputField.defaultProps = {
    placeholder: '',
};

export default InputField;
