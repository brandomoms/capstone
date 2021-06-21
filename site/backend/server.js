const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');
const { log, ExpressAPILogMiddleware } = require('@rama41222/node-logger');
const fs = require('fs');

const config = {
    name: 'sample-express-app',
    port: 3000,
    host: '0.0.0.0'
};

const app = express();
const logger = log({ console: true, file: false, label: config.name });

// const split_test_init = splitTestInit();

// var main_model_flagged = [];
// var test_model_flagged = [];

app.use(bodyParser.json());
app.use(cors());
app.use(ExpressAPILogMiddleware(logger, { request: true }));


app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname + '/index.html'));
});

// app.get('/:ex', (req, res) => {
//     if (req.params.ex === "1") {
//         res.sendFile(path.join(__dirname + '/index_e1.html'));
//     } else if (req.params.ex === "2") {
//         res.sendFile(path.join(__dirname + '/index_e2.html'));
//     }
//
// });

app.get('/data', (req, res) => {
    res.sendFile(path.join(__dirname + '/model/data.json'));
});

//
// app.get('/data_e1', (req, res) => {
//     res.sendFile(path.join(__dirname + '/model/data_e1.json'));
// });
//
//
// app.get('/data_e1', (req, res) => {
//     res.sendFile(path.join(__dirname + '/model/data_e2.json'));
// });


app.get('/images/:cam', (req, res) => {
    res.sendFile(path.join(__dirname + `/model/imagestore/official/${req.params.cam}`))
});


app.post('/flag/:cam', (req, res) => {
  let datastore = JSON.parse(fs.readFileSync(path.join(__dirname + '/model/data.json'), 'utf8'));
  let curr_image_path = path.join(__dirname + `/model/imagestore/official/${req.params.cam}`);
  let d = datastore[req.params.cam];
  let newclass = (d.hazardous === "1") ? "0" : "1";
  let new_image_path = path.join(__dirname + `/model/imagestore/train/${d.fhash}_${req.params.cam.slice(0,-4)}_${newclass}.jpg`);
  console.log("image path ", curr_image_path); console.log("copy path ", new_image_path);
  if (fs.existsSync(new_image_path)) {
      res.send('image already flagged as incorrect');
  }

  else {
      fs.createReadStream(curr_image_path).pipe(fs.createWriteStream(new_image_path));
      res.send('flagged image as incorrect');
  }
});


app.listen(config.port, config.host, (e)=> {
    if (e) {
        throw new Error('Internal Server Error');
    }
    logger.info(`${config.name} running on ${config.host}:${config.port}`);
});
