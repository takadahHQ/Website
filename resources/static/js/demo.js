(function () {
  "use strict";

  // Input tags
  const myTagify = function () {
    // tagify
    const input_tags = document.querySelectorAll("input.tagify");

    if ( input_tags != null) {
      for( let i = 0; i < input_tags.length; i++)
      {
        new Tagify(input_tags[i]);
      }
    }
  }


  // Custom JS
  const myCustom = function () {

    // insert your custom javascript on here
    
  }

  /**
   * ------------------------------------------------------------------------
   * Launch Functions
   * ------------------------------------------------------------------------
   */
  myTagify();
  myCustom();

})();