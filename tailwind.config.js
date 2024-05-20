/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      backgroundImage:{
        'custom-background' : "url('https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg?cs=srgb&dl=pexels-pixabay-531880.jpg&fm=jpg')"
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],

  
}

