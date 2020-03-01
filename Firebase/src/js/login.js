(function() {
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
})();

firebase.auth().onAuthStateChanged(function(user) {
  if (user == null) {
    console.log("Error");
    return;
  } else {
    userId = user.uid;
    // you can also get .displayName, .photoURL, .email
    console.log(userId);
    window.location.href = "stats.html";
  }
});

function loadIn() {
  document.getElementById("email").value = "";
  document.getElementById("password").value = "";
  firebase.auth().signOut();
  console.log("not logged in");

  if (firebase.auth().currentUser) {
    firebase.auth().signOut();
    console.log("Last user logged out");
  }

  //   if (firebase.auth().currentUser) {
  //     firebase.auth().signOut();
  //     console.log("Last user logged out");
  //   } else {
  //     console.log("No user logged in");
  //   }
}

function login() {
  if (firebase.auth().currentUser) {
    firebase.auth().signOut();
    console.log("Last user logged out");
  } else {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    // Check for email length
    if (email.length < 4) {
      alert("Please enter an email address.");
      return;
    } //end email length check

    // Check for password length
    if (password.length < 4) {
      alert("Please enter a password.");
      return;
    } //end password length check

    // Sign in with email and pass.

    firebase
      .auth()
      .signInWithEmailAndPassword(email, password)
      .catch(function(error) {
        // Error Handler
        var errorCode = error.code;
        var errorMessage = error.message;

        if (errorCode === "auth/wrong-password") {
          alert("Wrong password.");
        } else {
          alert(errorMessage);
        }

        console.log(error);
      }); //end firebase.auth() //end if-else
  } //end toggle function
}

/////////////////// SIGNIN FUNCTION //////////////////

function signin() {
  const provider = new firebase.auth.GoogleAuthProvider();
  firebase.auth().signInWithPopup(provider);
}
