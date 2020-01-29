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

  const gp = document.getElementById("gp").value;
  const pts = document.getElementById("pts").value;
  const ason = document.getElementById("ason").value;
  const ah = document.getElementById("ah").value;
  const pp = document.getElementById("pp").value;
  const sp = document.getElementById("sp").value;

  const data = {
    GamesPlayed: gp,
    Points: pts,
    ASON: ason,
    AH: ah,
    PuckPossession: pp,
    SaveP: sp
  };

  ref.set(data);
  document.getElementById("gp").value = "";
  document.getElementById("pts").value = "";
  document.getElementById("ason").value = "";
  document.getElementById("ah").value = "";
  document.getElementById("pp").value = "";
  document.getElementById("sp").value = "";

  alert("Data Updated");
  window.location.reload();
  console.log("Updated");
}

function tableLoad() {
  const teamSelect = document.getElementById("teamSelect");
  const team = teamSelect.options[teamSelect.selectedIndex].value;

  const array = [];

  const ref = firebase.database().ref(team);
  ref.once("value").then(_team => {
    _team.forEach(_teamStats => {
      const teamStats = _teamStats.val();

      console.log(typeof teamStats);
      var obj = JSON.parse(teamStats);
      console.log(obj);
      array.push(teamStats);
      //                                                      \\
      //                                                      \\
      //                                                      \\
      //                                                      \\

      // console.log(AGP, APTS, AASON, AAH, AP, ASP);
    });
  });

  console.log(array);
  // const arrayLength = array.length;

  // for (var i = 0; i < arrayLength; i++);
  // {
  //   console.log(array[i]);
  // }
  // console.log(array);

  const AGP = document.getElementById("AGP");
  const APTS = document.getElementById("APTS");
  const AASON = document.getElementById("AASON");
  const AAH = document.getElementById("AAH");
  const AP = document.getElementById("AP");
  const ASP = document.getElementById("ASP");

  // ||||||||||||||||||||||||||||||||||||\\

  document.getElementById("AGP").value;
  document.getElementById("APTS");
  document.getElementById("AASON");
  document.getElementById("AAH");
  document.getElementById("AP");
  document.getElementById("ASP");
}

// function tableLoad() {
//   const fragment = document.createDocumentFragment();
//   const table = document.createElement("table");

//   const query = firebase.database().ref("Team 1");

//   query.once("value").then(function(snapshot) {
//     snapshot.forEach(function(childSnapshot) {
//       var tr = document.createElement("tr");
//       var trValues = [childSnapshot.key, childSnapshot.val()];

//       for (var i = 0; i < trValues.length; i++) {
//         var td = document.createElement("td");

//         td.textContent = trValues[i];
//         tr.appendChild(td);
//       }

//       table.appendChild(tr);
//     });
//   });

//   fragment.appendChild(table);
//   document.body.appendChild(fragment);
//   console.log("bruh");
// }
