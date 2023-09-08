$(document).ready(function() {
        
    // Function to adjust the card heights
    function adjustCardHeights() {
        // Reset all card heights to auto first
        $('.uni-card').css('height', 'auto');

        // Find the tallest card
        var tallestCard = 0;
        $('.uni-card').each(function() {
            if ($(this).height() > tallestCard) {
                tallestCard = $(this).height();
            }
        });

        // Set all cards to the height of the tallest card
        $('.uni-card').height(tallestCard);
    }

    // Call the function initially
    adjustCardHeights();

    // Call the function whenever the window is resized
    $(window).resize(adjustCardHeights);
});