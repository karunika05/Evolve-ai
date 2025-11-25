
const themes = { 
  light: {
        background: '#e8f0ff',
        text: '#003366',
        nav: '#cfe0ff',
        hero: '#dce8ff',
        card: '#f0f6ff',
        palette: ['#4d79ff', '#80aaff', '#b3ccff']
    },
    dark: {
        background: '#181818',
        text: '#ffffff',
        nav: '#222222',
        hero: '#333333',
        card: '#2a2a2a',
        palette: ['#555555', '#777777', '#999999']
    },
    tropical: {
        background: '#fff4e0',
        text: '#b35400',
        nav: '#ffd8a8',
        hero: '#ffe5c2',
        card: '#fff0db',
        palette: ['#ff8c42', '#ffa75e', '#ffc799']
    }
};

function setTheme(themeName) {
    const theme = themes[themeName];

    // Update Page Background and Text
    document.body.style.background = theme.background;
    document.body.style.color = theme.text;

    // Update Navbar
    const nav = document.querySelector('nav');
    nav.style.background = theme.nav;
    nav.style.color = theme.text;

    // Update Hero Section
    const hero = document.querySelector('.hero');
    hero.style.background = theme.hero;
    hero.style.color = theme.text;

    // Update Feature Cards
    const cards = document.querySelectorAll('.feature-card');
    cards.forEach(card => {
        card.style.background = theme.card;
        card.style.color = theme.text;
    });

    // Update Color Palette Boxes
    document.querySelector('.box1').style.background = theme.palette[0];
    document.querySelector('.box2').style.background = theme.palette[1];
    document.querySelector('.box3').style.background = theme.palette[2];
}