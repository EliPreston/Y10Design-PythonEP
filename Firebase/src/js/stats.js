var config = {
  apiKey: "AIzaSyCFMw8Iu6LR93V03f-KiZpWyaGddSmJm3U",
  authDomain: "versace-9358b.firebaseapp.com",
  databaseURL: "https://versace-9358b.firebaseio.com",
  projectId: "versace-9358b",
  storageBucket: "versace-9358b.appspot.com",
  messagingSenderId: "327362565584",
  appId: "1:327362565584:web:e0f5dc27ac440b614315d5",
  measurementId: "G-H2Q57Q6XTB"
};

firebase.initializeApp(config);

function update() {
  var database = firebase.database();

  const teamSelect = document.getElementById("teamSelect");
  const team = teamSelect.options[teamSelect.selectedIndex].value;
  console.log(team);

  const ref = firebase.database().ref(team);
  ref.once("value").then(_team => {
    _team.forEach(_teamStats => {
      const teamStats = _teamStats.val();
    });
  });

  valueArray = [];
  const gp = document.getElementById("gp").value;
  const pts = document.getElementById("pts").value;
  const ason = document.getElementById("ason").value;
  const ah = document.getElementById("ah").value;
  const pp = document.getElementById("pp").value;
  const sp = document.getElementById("sp").value;

  valueArray.push(gp, pts, ason, ah, pp, sp);
  console.log(valueArray);

  count = 0;
  for (i = 0; i < valueArray.length; i++) {
    console.log(valueArray[i]);

    if (valueArray[i] === "") {
      alert("The database won't be updated if any of the text boxes are empty");
      count += 1;
    }
  }

  if (count === 0) {
    const data = {
      GamesPlayed: gp,
      Points: pts,
      ASON: ason,
      AH: ah,
      PuckPossession: pp,
      SaveP: sp
    };
    ref.set(data);
  }

  // resets input fields
  document.getElementById("gp").value = "";
  document.getElementById("pts").value = "";
  document.getElementById("ason").value = "";
  document.getElementById("ah").value = "";
  document.getElementById("pp").value = "";
  document.getElementById("sp").value = "";

  console.log("Updated");
  alert("Data Updated");

  window.location.reload();
}

function tableLoad() {
  const database = firebase.database();
  const myTable = document.getElementById("myTable");

  stRef1 = database.ref("Team 1");
  stRef1.once("value").then(_team => {
    // console.log(_team.val());
    const stats = _team.val();
    // console.log(stats.AH);
    // console.log(stats.ASON);
    // console.log(stats.GamesPlayed);
    // console.log(stats.Points);
    // console.log(stats.PuckPossession);
    // console.log(stats.SaveP);

    myTable.rows[1].cells[1].innerHTML = stats.AH;
    myTable.rows[1].cells[2].innerHTML = stats.ASON;
    myTable.rows[1].cells[3].innerHTML = stats.GamesPlayed;
    myTable.rows[1].cells[4].innerHTML = stats.Points;
    myTable.rows[1].cells[5].innerHTML = stats.PuckPossession;
    myTable.rows[1].cells[6].innerHTML = "." + stats.SaveP;
  });

  stRef2 = database.ref("Team 2");
  stRef2.once("value").then(_team => {
    // console.log(_team.val());
    const stats = _team.val();
    // console.log(stats.AH);
    // console.log(stats.ASON);
    // console.log(stats.GamesPlayed);
    // console.log(stats.Points);
    // console.log(stats.PuckPossession);
    // console.log(stats.SaveP);

    myTable.rows[2].cells[1].innerHTML = stats.AH;
    myTable.rows[2].cells[2].innerHTML = stats.ASON;
    myTable.rows[2].cells[3].innerHTML = stats.GamesPlayed;
    myTable.rows[2].cells[4].innerHTML = stats.Points;
    myTable.rows[2].cells[5].innerHTML = stats.PuckPossession;
    myTable.rows[2].cells[6].innerHTML = "." + stats.SaveP;
  });

  stRef3 = database.ref("Team 3");
  stRef3.once("value").then(_team => {
    // console.log(_team.val());
    const stats = _team.val();
    // console.log(stats.AH);
    // console.log(stats.ASON);
    // console.log(stats.GamesPlayed);
    // console.log(stats.Points);
    // console.log(stats.PuckPossession);
    // console.log(stats.SaveP);

    myTable.rows[3].cells[1].innerHTML = stats.AH;
    myTable.rows[3].cells[2].innerHTML = stats.ASON;
    myTable.rows[3].cells[3].innerHTML = stats.GamesPlayed;
    myTable.rows[3].cells[4].innerHTML = stats.Points;
    myTable.rows[3].cells[5].innerHTML = stats.PuckPossession;
    myTable.rows[3].cells[6].innerHTML = "." + stats.SaveP;
  });

  stRef4 = database.ref("Team 4");
  stRef4.once("value").then(_team => {
    // console.log(_team.val());
    const stats = _team.val();
    // console.log(stats.AH);
    // console.log(stats.ASON);
    // console.log(stats.GamesPlayed);
    // console.log(stats.Points);
    // console.log(stats.PuckPossession);
    // console.log(stats.SaveP);

    myTable.rows[4].cells[1].innerHTML = stats.AH;
    myTable.rows[4].cells[2].innerHTML = stats.ASON;
    myTable.rows[4].cells[3].innerHTML = stats.GamesPlayed;
    myTable.rows[4].cells[4].innerHTML = stats.Points;
    myTable.rows[4].cells[5].innerHTML = stats.PuckPossession;
    myTable.rows[4].cells[6].innerHTML = "." + stats.SaveP;
  });

  stRef5 = database.ref("Team 5");
  stRef5.once("value").then(_team => {
    // console.log(_team.val());
    const stats = _team.val();
    // console.log(stats.AH);
    // console.log(stats.ASON);
    // console.log(stats.GamesPlayed);
    // console.log(stats.Points);
    // console.log(stats.PuckPossession);
    // console.log(stats.SaveP);

    myTable.rows[5].cells[1].innerHTML = stats.AH;
    myTable.rows[5].cells[2].innerHTML = stats.ASON;
    myTable.rows[5].cells[3].innerHTML = stats.GamesPlayed;
    myTable.rows[5].cells[4].innerHTML = stats.Points;
    myTable.rows[5].cells[5].innerHTML = stats.PuckPossession;
    myTable.rows[5].cells[6].innerHTML = "." + stats.SaveP;
  });

  var coll = document.getElementsByClassName("collapsible");
  var i;

  for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var content = this.nextElementSibling;
      if (content.style.maxHeight) {
        content.style.maxHeight = null;
      } else {
        content.style.maxHeight = content.scrollHeight + "px";
      }
    });
  }
}
