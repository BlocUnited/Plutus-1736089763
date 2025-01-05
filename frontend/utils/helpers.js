export const validateEmail = (email) => {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(String(email).toLowerCase());
};

export const formatDate = (date) => {
    return new Date(date).toLocaleDateString('en-US');
};

export const validatePasswordStrength = (password) => {
    return password.length >= 8;
};
