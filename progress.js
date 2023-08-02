const thisYear = new Date().getFullYear()
const startTimeOfThisYear = new Date(`${thisYear}-01-01T00:00:00+00:00`).getTime()
const endTimeOfThisYear = new Date(`${thisYear}-12-31T23:59:59+00:00`).getTime()
const progressOfThisYear = (Date.now() - startTimeOfThisYear) / (endTimeOfThisYear - startTimeOfThisYear)
const progressBarOfThisYear = generateProgressBar()

function generateProgressBar() {
    const progressBarCapacity = 30
    const passedProgressBarIndex = parseInt(progressOfThisYear * progressBarCapacity)
    const progressBar = Array(progressBarCapacity)
        .fill('▁')
        .map((value, index) => index < passedProgressBarIndex ? '█' : value)
        .join('')
    return `{ ${progressBar} }`
}

const readme = `\
### Hi there <img src='https://qpluspicture.oss-cn-beijing.aliyuncs.com/6LjjQA/Hi.gif' alt='Hi' width="24"/>
⏳ Year progress ${progressBarOfThisYear} ${(progressOfThisYear * 100).toFixed(2)} %
![donniesky's github stats](https://bad-apple-github-readme.vercel.app/api?show_bg=1&username=donniesky&show_icons=true&theme=dracula)
- 🔭 I’m currently working on Weeget
- 🎓 I’m graduated at Renmin University of China
- 🌱 I’m currently learning Flutter
- 👯 I’m looking to collaborate on anything about Android
- 💬 Ask me about everything you want talk with me
- 📫 How to reach me: https://t.me/donnieSky
- 😄 Pronouns: Action speak louder than words!
- ⚡ Fun fact: 👫 🐶 🐈 :octocat: 🏀 🚴 🎮 :hearts: 🍚 ✈️
[<img src="https://img.shields.io/badge/Twitter-%40donniesky-blue">](https://twitter.com/donnieSky815)
[<img src="https://img.shields.io/badge/Email-donniesky.me%40gmail.com-orange">](mailto:donniesky.me@gmail.com)
---
⏰ Updated on ${new Date().toUTCString()}
![Progress Bar CI](https://github.com/donniesky/donniesky/workflows/Progress%20Bar%20CI/badge.svg)\
`

console.log(readme)
	
