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
    window.location.href = "home.html";
    return;
  } else {
    userId = user.uid;
    email = user.email;
    document.getElementById("userinfo1").innerHTML = userId;
    document.getElementById("userinfo2").innerHTML = email;

    // you can also get .displayName, .photoURL, .email
    console.log(userId);
    console.log(email);
  }
});

function accountLogout() {
  console.log("logging out");
  firebase.auth().signOut();
  window.location.href = "home.html";
}
