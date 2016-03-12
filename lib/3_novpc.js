/**
 * Lib
 */
module.exports.respond = function(event, cb) {
    var response = {
      message: "Your Message: " + event.text
    };
    return cb(null, response);
};
