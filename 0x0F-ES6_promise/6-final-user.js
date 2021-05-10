// Some random doc
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([
    uploadPhoto(fileName),
    signUpUser(firstName, lastName),
  ]).then(() => {
  }).catch(() => {
  }).finally((values) => values);
}
