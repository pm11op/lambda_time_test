/**
 * Lib
 */
var mysql = require('mysql');
var mysqlconfig = JSON.parse(process.env.mysqlconfig);
var pool = mysql.createPool({
  host     : mysqlconfig.host,
  user     : mysqlconfig.user,
  password : mysqlconfig.password,
  database : mysqlconfig.db,
  acquireTimeout: 1000
});
  pool.getConnection(function(err, connection) {
    connection.query("insert into lambda_test values(0, ?, NOW())", 'init', function(err, re) {
    if (err) throw err;
    connection.release();
  });
  });
module.exports.respond = function(event, cb) {
  pool.getConnection(function(err, connection) {
    connection.query("insert into lambda_test values(0, ?, NOW())", [event.text], function(err, re) {
    if (err) throw err;
    connection.release();
    var response = {
      message: "Your Message: " + event.text
    };
    return cb(null, response);
    });
  });
};
