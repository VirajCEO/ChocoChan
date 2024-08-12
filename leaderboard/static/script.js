document.addEventListener('DOMContentLoaded', function () {
    const list = document.getElementById('list');
    const winnerCard = document.getElementById('winner');

    fetch('/team')
        .then(response => response.json())
        .then(data => {
            data.forEach(member => {
                let newRow = document.createElement('li');
                newRow.classList = 'c-list__item';
                newRow.innerHTML = `
                    <div class="c-list__grid">
                        <div class="c-flag c-place u-bg--transparent">${member.rank}</div>
                        <div class="c-media">
                            <img class="c-avatar c-media__img" src="${generateInitialsAvatar(member.name)}" />
                            <div class="c-media__content">
                                <div class="c-media__title">${member.name}</div>
                                <a class="c-media__link u-text--small2" target="_blank">${member.handle}</a>
                            </div>
                        </div>

                        <div class="u-text--right c-kudos">
                            <div class="u-mt--8">
                                <strong>${member.kudos}</strong> ${randomEmoji()}
                            </div>
                        </div>
                    </div>
                `;
                if(member.rank === 1) {
                    newRow.querySelector('.c-place').classList.add('u-text--dark')
                    newRow.querySelector('.c-place').classList.add('u-bg--yellow')
                    newRow.querySelector('.c-kudos').classList.add('u-text--yellow')
                } else if(member.rank === 2) {
                    newRow.querySelector('.c-place').classList.add('u-text--dark')
                    newRow.querySelector('.c-place').classList.add('u-bg--teal')
                    newRow.querySelector('.c-kudos').classList.add('u-text--teal')
                } else if(member.rank === 3) {
                    newRow.querySelector('.c-place').classList.add('u-text--dark')
                    newRow.querySelector('.c-place').classList.add('u-bg--orange')
                    newRow.querySelector('.c-kudos').classList.add('u-text--orange')
                }
                list.appendChild(newRow)
            })

            // Find Winner from sent kudos
            let sortedTeam = data.sort((a, b) => b.sent - a.sent)
            let winner = sortedTeam[0]

            // Render winner card
            winnerCard.innerHTML = `
                <img class="c-avatar c-avatar--lg" src="${generateInitialsAvatar(winner.name)}"/>
                <h3 class="u-mt--16">${winner.name}</h3>
                <span class="u-text--teal u-text--small">${winner.name}</span>
            `
        });
    function generateInitialsAvatar(name) {
            const initials = name.split(' ').map(word => word.charAt(0)).join('');
            const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
            const canvas = document.createElement('canvas');
            const context = canvas.getContext('2d');
            canvas.width = 100;
            canvas.height = 100;
        
            // Draw background
            context.fillStyle = randomColor;
            context.fillRect(0, 0, canvas.width, canvas.height);
        
            // Draw initials
            context.fillStyle = '#FFFFFF';
            context.font = 'bold 50px Arial';
            context.textAlign = 'center';
            context.textBaseline = 'middle';
            context.fillText(initials, canvas.width / 2, canvas.height / 2);
        
            return canvas.toDataURL();
        }
        
    function randomEmoji() {
        const emojis = [''];
        let randomNumber = Math.floor(Math.random() * emojis.length);
        return emojis[randomNumber]
    }

});

