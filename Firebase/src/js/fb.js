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

const signup = () => {
  let newUser = undefined;
  let ableToCreateUser = false;
  const firstName = document.getElementById("firstName").value;
  const lastName = document.getElementById("lastName").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  firebase
    .auth()
    .createUserWithEmailAndPassword(email, password)
    .catch(err => {
      alert(`Uh oh! Poopee! | ${err.code}: ${err.message}`);
      ableToCreateUser = false;
    })
    .then(user => {
      if (ableToCreateUser) {
        newUser = {
          firstName,
          lastName,
          email,
          password
        };
      }
    })
    .then(() => {
      if (ableToCreateUser) {
        firebase
          .database()
          .ref("/users")
          .push(newUser);
      }
    });
  //   const firstName = document.getElementById("firstName").value;
  //   const lastName = document.getElementById("lastName").value;
  //   const email = document.getElementById("email").value;
  //   const password = document.getElementById("password").value;

  //   const user = {
  //     firstName,
  //     lastName,
  //     email,
  //     password
  //   };

  //   firebase
  //     .database()
  //     .ref("/users")
  //     .push(user)
  //     .then(() => {
  //       alert("Signed up!");
  //     })
  //     .catch(err => {
  //       alert(err.code, err.message);
  //     });
};
