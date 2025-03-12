/** @type {import('tailwindcss').Config} */
module.exports = {
content: [
    "../../templates/*.{js,ts,jsx,tsx,html}",
    "./src/**/*.{js,ts,jsx,tsx}",
    "../../templates/**/*.{js,ts,jsx,tsx,html}",
],
  theme: {
        extend: {
            colors: {
                twicePink: '#F28EB2',
                reveluvWendy: '#007aff'
            },
            fontFamily: {
                giga: 'Oranienbaum',
                main: 'Montserrat'
            }
        },
    },
  plugins: [],
}

