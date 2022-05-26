let qrxtendCustomers = {
    antik: "https://qr-xtend.de/show_file_preview/96ef98be-fa47-4e33-860c-dc4bc187241e",
    xaza: "https://qr-xtend.de/show_file_preview/5e3e0cac-3bbe-4663-a4d9-d359c49777b3",
};

redirectToQrxtend();

function redirectToQrxtend() {
    let searchParams = new URLSearchParams(window.location.search);
    if (searchParams.has('card')) {
        let card = searchParams.get('card');
        if (card in qrxtendCustomers) {
            window.location.href = qrxtendCustomers[card];
            window.location.replace(qrxtendCustomers[card]);
        }
    }
}
