let cards = {
    antik: "Antik Karte.pdf"
}

$(document).ready(function() {
    $(".progress, .meter")
        .animate({
            opacity: 1
        }, 1900)
        .animate({
                backgroundColor: "#ffffff",
            }, 2000);

    small_height = 60;
    small_width = 60;
    big_height = 62;
    big_width = 62;

    top_offset = -10;

    small_size_height = small_height + "%";
    small_size_width = small_width + "%";
    big_size_height = big_height + "%";
    big_size_width = big_width + "%";

    left_small = (100 - small_width) / 2 + "%";
    top_small = top_offset + (100 - small_height) / 2 + "%";
    left_big = (100 - big_width) / 2 + "%";
    top_big = top_offset + (100 - big_height) / 2 + "%";

    $(".img")
        .animate({
            left: left_small,
            top: top_small,
            width: small_size_width,
            height: small_size_height
        }, 0)
        .animate({
            width: small_size_width,
            height: small_size_height
        }, 200)
        .animate({
            left: left_big,
            top: top_big,
            width: big_size_width,
            height: big_size_height
        }, 800, "swing")
        .animate({
            left: left_small,
            top: top_small,
            width: small_size_width,
            height: small_size_height
        }, 800)
        .animate({
            left: left_big,
            top: top_big,
            width: big_size_width,
            height: big_size_height
        }, 1100, function() {
            loadPdf();
        });
});

function loadPdf() {
    let searchParams = new URLSearchParams(window.location.search);
    if (searchParams.has('card')) {
        let card = searchParams.get('card');
        window.location.href = cards[card];
        window.location.replace(cards[card]);
    }
}
