// [START initialize_firebase_in_sw]
// Give the service worker access to Firebase Messaging.
// Note that you can only use Firebase Messaging here, other Firebase libraries
// are not available in the service worker.
importScripts('https://www.gstatic.com/firebasejs/8.4.2/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.4.2/firebase-messaging.js');

// Initialize the Firebase app in the service worker by passing in the
// messagingSenderId.
const firebaseConfig = {
  apiKey: "AIzaSyC25pD8LmDREmyo4ktsljq6Pcfu_vpb-Kk",
  authDomain: "fcm-notification-3c344.firebaseapp.com",
  projectId: "fcm-notification-3c344",
  storageBucket: "fcm-notification-3c344.appspot.com",
  messagingSenderId: "536997301741",
  appId: "1:536997301741:web:de4672ce3959393b4bebe4"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);


// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();
// [END initialize_firebase_in_sw]

// If you would like to customize notifications that are received in the
// background (Web app is closed or not in browser focus) then you should
// implement this optional method.
// [START background_handler]
messaging.onBackgroundMessage((payload)=>{
  console.log('[firebase-messaging-sw.js] Received background message ', payload);
  // Customize notification here
  const notificationTitle = payload.notification.title;
  const notificationOptions = {
    body: payload.notification.body,
    icon: payload.data.icon_url,
    image: payload.data.image_url,
    badge: payload.data.image_url,
    data: { launch_url: payload.data.launch_url },
    requireInteraction: true,
    actions:  payload.data.launch_url ? [{ action: "launch_url", title: "Read Now" }] : [],
  }

  return self.registration.showNotification(
    notificationTitle, notificationOptions
  )
})
// [END background_handler]


// Code added from old aplustopper project
self.addEventListener("notificationclick", (event)=>{
  console.log("On notification click: ", event);

  const launch_url = event.notification.data.launch_url

  // Android doesn't close the notification when you click on it
  event.notification.close();

  // This looks to see if the current is already open and
  // focuses if it is
  event.waitUntil(
    clients.matchAll({ type: "window" })
      .then((clientList)=>{
        // Check if there is already a window/tab open with the target URL
        for (var i = 0; i < clientList.length; i++) {
          var client = clientList[i];
          if (client.url == launch_url && "focus" in client) {
              return client.focus()
            }
        }
        // If not, then open the target URL in a new window/tab.
        if (clients.openWindow && launch_url) {
          return clients.openWindow(launch_url);
        }
      })
  );
});
