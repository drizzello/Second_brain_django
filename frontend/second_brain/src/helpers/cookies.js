/**
 * Recupera il valore di un cookie dal nome.
 * @param {string} name - Il nome del cookie da cercare
 * @returns {string|undefined} Il valore del cookie, o undefined se non trovato
 */
export const getCookie = (name) => {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
};