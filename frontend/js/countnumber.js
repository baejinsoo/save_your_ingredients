function dispCount(counters) {
    // var counters = $('.counter');
    const speed = 300;
    counters.each((index, counter) => {
        const updateCount = () => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText;

            const inc = target / speed;

            if(count < target) {
                counter.innerText = Math.ceil(count + inc);
                setTimeout(updateCount, 1);
            } else {
                count.innerText = target;
            }
        }

        updateCount();
    })
}