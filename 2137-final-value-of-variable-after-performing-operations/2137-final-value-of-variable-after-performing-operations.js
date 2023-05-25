/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let num = 0;
    operations.forEach(operation => {
        if (operation == "++X" || operation == "X++"){
            num++;
        }
        else if (operation == "--X" || operation == "X--"){
            num--;
        }
    })
    return num;
};