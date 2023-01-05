function set_color () {
    "use strict";
    const cards = ["card1", "card2",  "card3",  "card4",  "card5"];
    const colors = ["#ADC5CF","#D5CABD","#FEFEDF","#009184","#95B0B2","#F9FBE7","#009198","#B1BB77","#C3FCF2","#00283B","#D3FBD8","#F4EFF8","#D3FBD8",];
    cards.map((card) => document.getElementById(card).style = `color : red; background-color: ${colors[Math.floor(Math.random() * (colors.length - 1 ))]};`);
}