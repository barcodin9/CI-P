import Clerk from "@clerk/clerk-js";

const clerkPubKey = "pk_test_Y2hlZXJmdWwtbGFtcHJleS0zNS5jbGVyay5hY2NvdW50cy5kZXYk";
 
const clerk = new Clerk(clerkPubKey);
await clerk.load({
  // Set load options here
});

if (clerk.user) {
  document.getElementById("app").innerHTML = `
    <div id="user-button"></div>
  `;
 
  const userButtonDiv =
    document.getElementById("user-button");
 
  clerk.mountUserButton(userButtonDiv);
} else {
  document.getElementById("app").innerHTML = `
    <div id="sign-in"></div>
  `;
 
  const signInDiv =
    document.getElementById("sign-in");
 
  clerk.mountSignIn(signInDiv);
}