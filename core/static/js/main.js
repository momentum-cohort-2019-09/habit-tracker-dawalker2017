let buttons = document.getElementsByClassName('log_button')

function delete_logs() {
    for (button of buttons) {
        button.addEventListener('click', function(event, pk) {
            console.log('clicked')
            let el = event.target
            let deckpk = el.dataset.logPk
            fetch('delete_log/' + logpk, {
                method: 'POST'
            }).then(res => {
                if (res.ok) {
                    event.target.closest('.main_page_container_log').remove()
                }
            })
        });
    }
}

delete_logs()