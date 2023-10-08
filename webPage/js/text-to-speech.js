function initializeTTS() {
    const domPage = document.getElementById('content');
    const listenText = '🔈 Listen to this page';
    const stopText = '🔈 Stop speech';
    const res = {};
    let text = document.getElementById('content').textContent;

    console.log(text);
    const msg = new SpeechSynthesisUtterance(text);
    msg.lang = 'en-us';

    res.speak = () => {
        speechSynthesis.speak(msg);
    }

    res.pause = () => {
        speechSynthesis.pause();
    }

    res.stop = () => {
        speechSynthesis.cancel();
    }

    document.addEventListener('loads', res.stop());

    const ttsButtons = document.getElementsByClassName('ttsBtn');
    for (const b of ttsButtons) {
        b.innerHTML = listenText;

        b.addEventListener('click', () => {
            if (!speechSynthesis.speaking) {
                b.innerHTML = stopText;
                res.speak();
            } else {
                b.innerHTML = listenText;
                res.stop();
            }
        });
    }

    return res;
}