// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "AIzaSyC25pD8LmDREmyo4ktsljq6Pcfu_vpb-Kk",
  authDomain: "fcm-notification-3c344.firebaseapp.com",
  projectId: "fcm-notification-3c344",
  storageBucket: "fcm-notification-3c344.appspot.com",
  messagingSenderId: "536997301741",
  appId: "1:536997301741:web:de4672ce3959393b4bebe4"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const messaging = firebase.messaging()

function subscribe(){
  notifyMe()
  messaging.getToken()
  .then((token)=>{
    console.log(token)
    showTokenInUI(token)

    if (isTokenSentToServer()){
      console.log('Already sent to the server.')
    } else {
      sendTokenToServer(token)
    }
  })
  .catch((err)=>{
    console.log(`Error getting token: ${err}`)
  })
}

messaging.onMessage((payload)=>{
  console.log(`Message Payload: `,payload)
  $('#liveToast .toast-icon').attr('src', payload.notification.icon)
  $('#liveToast .toast-title').text(payload.notification.title)
  $('#liveToast .toast-body').text(payload.notification.body)
  $('#liveToast').toast('show')
})



// Send the Instance ID token your application server, so that it can:
// - send messages back to this app
// - subscribe/unsubscribe the token from topics
function sendTokenToServer(token) {
  console.log('Sending token to server...');
  // TODO(developer): Send the current token to your server.
  fetch('http://localhost:8000/api/fcm/device/create/', {
    method: "POST",
    headers: {
        'Content-Type': 'application/json',
        // 'X-CSRFToken': '{{ csrf_token }}'
      },
    body: JSON.stringify({
      'registration_id': token,
      'type': 'web',
    }),
    // credentials: "include",
  }).then(function(response) {
    console.log(response);
    if(response.ok=true) {
      setTokenSentToServer(true);
    }
  })
}

function setTokenSentToServer(sent) {
  if (sent) {
    window.localStorage.setItem('sentToServer', 1);
  } else {
    window.localStorage.setItem('sentToServer', 0);
  }
}


function isTokenSentToServer() {
  if (window.localStorage.getItem('sentToServer') == '1') {
        return true;
  }
  return false;
}


function showTokenInUI(token){
  const tokenElement = document.getElementById('token')
  tokenElement.innerHTML = token
  tokenElement.style.overflowWrap = 'break-word'
}

function notifyMe() {
  // Let's check if the browser supports notifications
  if (!("Notification" in window)) {
    alert("This browser does not support desktop notification");
  }

  // Otherwise, we need to ask the user for permission
  if (Notification.permission === "denied" || Notification.permission === "default") {
    Notification.requestPermission()
      .then((permission)=>{
        console.log('Status of notification', permission)
      })
      .catch((err)=>{
        console.log('error in getting notification permission', err)
      })
  }
}

window.onload = function() {
  subscribe()
};