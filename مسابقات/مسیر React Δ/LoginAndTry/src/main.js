// use this function to send a login request
const login = require('./login');

async function loginAndTry(username, retry) {
  let t = 0,
    a = 0;

  while (a < retry) {
    a++;
    try {
      const res = await login(username);
      t += res.responseTime;
      return { try: a, status: true, timeSpent: t };
    } catch (err) {
      t += err.responseTime;
      if (a === retry) {
        return { try: a, status: false, timeSpent: t };
      }
    }
  }
}

module.exports = loginAndTry;
