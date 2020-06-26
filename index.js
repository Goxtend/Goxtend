let cards = {
    antik: "Antik Karte.pdf"
}

$(document).ready(function() {
    $(".overlay")
        .animate({ opacity: 1 }, 2000)
        .animate({ opacity: 0 }, 2000);
    
    $(".progress, .meter")
        .animate({
            opacity: 1}, 1900)
        .animate({
            backgroundColor: "#ffffff",
            opacity: 0}, 2000);

    small_size = "50%";
    big_size = "52%"

    $(".img")
        .animate({
            opacity: 1,
            width: small_size,
            height: small_size
        }, 200)
        .animate({
            opacity: 1,
            left: "24%",
            top: "14%",
            width: big_size,
            height: big_size
        }, 800, "swing")
        .animate({
            opacity: 1,
            left: "25%",
            top: "15%",
            width: small_size,
            height: small_size
        }, 800)
        .animate({
            opacity: 0,
            left: "0%",
            top: "0%",
            width: "100%",
            height: "100%"
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
