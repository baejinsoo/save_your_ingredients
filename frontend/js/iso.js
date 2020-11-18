// filter functions
var filterFns = {
  greaterThan50: function() {
    var number = $(this).find('.number').text();
    return parseInt( number, 10 ) > 50;
  },
  even: function() {
    var number = $(this).find('.number').text();
    return parseInt( number, 10 ) % 2 === 0;
  }
};

// store filter for each group
var filters = {};

// init Isotope
var $grid = $('.grid').isotope({
  itemSelector: '.color-shape',
  filter: function() {

    var isMatched = true;
    var $this = $(this);

    for ( var prop in filters ) {
      var filter = filters[ prop ];
      // use function if it matches
      filter = filterFns[ filter ] || filter;
      // test each filter
      if ( filter ) {
        isMatched = isMatched && $(this).is( filter );
      }
      // break if not matched
      if ( !isMatched ) {
        break;
      }
    }
    return isMatched;
  }
});



$('#filters').on( 'click', '.button', function() {
  var $this = $(this);
  // get group key
  var $buttonGroup = $this.parents('.button-group');
  var filterGroup = $buttonGroup.attr('data-filter-group');
  // set filter for group
  filters[ filterGroup ] = $this.attr('data-filter');
  // arrange, and use filter fn
  $grid.isotope();
});

// change is-checked class on buttons
$('.button-group').each( function( i, buttonGroup ) {
  var $buttonGroup = $( buttonGroup );
  $buttonGroup.on( 'click', 'button', function() {
    $buttonGroup.find('.is-checked').removeClass('is-checked');
    $( this ).addClass('is-checked');
  });
});