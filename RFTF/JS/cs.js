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

  document.getElementById("name").value = "";
  document.getElementById("comment").value = "";
  // This resets the input fields
}

function setData() {
  var database = firebase.database();
  var ref = database.ref("Comments");

  var name = document.getElementById("name").value;
  var comment = document.getElementById("comment").value;

  // This gets the value of the inputs and pushes them to an array

  valueArray = [];
  const nm = document.getElementById("name").value;
  const cmnt = document.getElementById("comment").value;
  valueArray.push(nm, cmnt);

  // This loops through the array and gets each object in the array
  // If either of the input boxes are empty, en alert pops up telling the use both inputs need to be filled out

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
  // Pushes data to firebase

  document.getElementById("name").value = "";
  document.getElementById("comment").value = "";
  // Resets input fields
}

function getData() {
  // This references Firebase, specifically the "Comments" node
  // After referencing that, this function calls another function below
  // If something goes wrong, the error function is called instead

  var database = firebase.database();
  var ref = database.ref("Comments");

  ref.on("value", gotData, errData);
}

function gotData(data) {
  // This is the helper function that is called by the previous "getData" function
  // Here, the function gets the commentList element
  // Then gets the data from Firebase, and loops through each one
  // For each new piece of data, an element is added to the list on the page
  document.getElementById("commentList").innerHTML = "";

  var commentData = data.val();
  // console.log(commentData);

  var keys = Object.keys(commentData);
  // console.log(keys);

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

// This is the error function
function errData(err) {
  console.log("Error!");
  console.log(err);
}
