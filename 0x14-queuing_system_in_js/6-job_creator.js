const kue = require('kue'),
      queue = kue.createQueue();

const jobData = {
  phoneNumber: 'string',
  message: 'string',
}

let job = queue
  .create('push_notification_code', jobData)
  .save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`)
    else console.log('Notification job failed');
  })
  .on('complete', () => console.log('Notification job failed'));
