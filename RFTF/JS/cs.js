function initializeApp() {
  var config = {
    apiKey: "AIzaSyDRGAhxSienEtC4WjKjNTREhhDzFux5UMA",
    authDomain: "rftf-1.firebaseapp.com",
    databaseURL: "https://rftf-1.firebaseio.com",
    projectId: "rftf-1",
    storageBucket: "rftf-1.appspot.com",
    messagingSenderId: "742173847323",
    appId: "1:742173847323:web:6cc7e23788a001d34cedbe",
    measurementId: "G-K5NEJM0LBS",
  };
  firebase.initializeApp(config);
  // console.log(firebase);

  document.getElementById("name").value = "";
  document.getElementById("comment").value = "";
}

function setData() {
  var database = firebase.database();
  var ref = database.ref("Comments");

  var name = document.getElementById("name").value;
  var comment = document.getElementById("comment").value;

  valueArray = [];
  const nm = document.getElementById("name").value;
  const cmnt = document.getElementById("comment").value;

  valueArray.push(nm, cmnt);

  count = 0;
  for (i = 0; i < valueArray.length; i++) {
    if (valueArray[i] === "") {
      alert(
        "You can't comment if one, or both, of the input boxes are empty. Thank you."
      );
      count += 1;
    }
  }

  if (count === 0) {
    var data = {
      Name: name,
      Comment: comment,
    };
  }

  ref.push(data);

  document.getElementById("name").value = "";
  document.getElementById("comment").value = "";

  // location.reload();
}

function getData() {
  var database = firebase.database();
  var ref = database.ref("Comments");

  ref.on("value", gotData, errData);
}

function gotData(data) {
  document.getElementById("commentList").innerHTML = "";

  var commentData = data.val();
  console.log(commentData);

  var keys = Object.keys(commentData);
  console.log(keys);

  for (var i = 0; i < keys.length; i++) {
    var k = keys[i];
    var name = commentData[k].Name;
    var comment = commentData[k].Comment;

    var oNames = document.getElementById("commentList");
    var entry = document.createElement("li");
    entry.appendChild(document.createTextNode(name + ": " + comment));
    oNames.appendChild(entry);
  }
}

function errData(err) {
  console.log("Error!");
  console.log(err);
}
