/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    darkMode: 'class',
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/resources), e.g. base.html. */
        '../templates/**/*.html',

        /* 
         * Main resources directory of the project (BASE_DIR/resources).
         * Adjust the following line to match your project structure.
         */
        '../../resources/**/*.html',
        
        /* 
         * Templates in other django apps (BASE_DIR/<any_app_name>/resources).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        '../../**/*.py'
    ],
    theme: {
      colors: {
        'mono': {
    '50': '#f7f7f7',
    '100': '#e3e3e3',
    '200': '#c8c8c8',
    '300': '#a4a4a4',
    '400': '#818181',
    '500': '#666666',
    '600': '#515151',
    '700': '#434343',
    '800': '#383838',
    '900': '#212121',
},
'rebel': {
    '50': '#fff0f0',
    '100': '#ffdede',
    '200': '#ffc2c2',
    '300': '#ff9898',
    '400': '#ff5c5c',
    '500': '#ff2a2a',
    '600': '#f80a0a',
    '700': '#d10404',
    '800': '#ac0808',
    '900': '#330505',
},
'tiber': {
    '50': '#eeffff',
    '100': '#c4f8ff',
    '200': '#89f1ff',
    '300': '#45e8ff',
    '400': '#10d2f1',
    '500': '#00b6d5',
    '600': '#0090ac',
    '700': '#006f88',
    '800': '#04566b',
    '900': '#052a33',
},
      // ...
    },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
        require("daisyui"),
    ],
}
