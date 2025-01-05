import React from 'react';
import PropTypes from 'prop-types';
import './Modal.css';

const Modal = ({ isVisible, onClose, title, content }) => {
    if (!isVisible) return null;

    return (
        <div className="modal-overlay">
            <div className="modal">
                <h2>{title}</h2>
                <div>{content}</div>
                <button onClick={onClose}>Close</button>
            </div>
        </div>
    );
};

Modal.propTypes = {
    isVisible: PropTypes.bool.isRequired,
    onClose: PropTypes.func.isRequired,
    title: PropTypes.string.isRequired,
    content: PropTypes.oneOfType([PropTypes.string, PropTypes.node]).isRequired,
};

export default Modal;
