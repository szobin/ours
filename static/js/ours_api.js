function get_token() {
  const e_token = $("input[name='csrfmiddlewaretoken']");
  return e_token.val();
}

function postRequest(url, data) {
  token = get_token();
  return fetch(url, {
    credentials: 'same-origin', // 'include', default: 'omit'
    method: 'POST', // 'GET', 'PUT', 'DELETE', etc.
    body: JSON.stringify(data), // Coordinate the body type with 'Content-Type'
    headers: new Headers({
      'Content-Type': 'application/json',
      'X-CSRFToken': token
    }),
  })
  .then(response => response.ok ?
     response.json() :
     {
       "error": `${response.status}: ${response.message}`,
       "status": -1
     })
}

let tableData = undefined;

function callLogAPI() {
   const table = $("table");
   const tableOpts = {
      paging: false,
      info: false
   }
   table.addClass('hidden');
   if (!tableData) {
     tableData = table.DataTable(tableOpts);
   }

   const log_text = $("textarea").val();
   const arg_data =    postRequest("api/log/process/", {
     log_text: log_text 
   }
   ).then(data => {
      if (data.status == 0) {
         console.log(data);
         const tableOpts = {
           paging: false,
           searching: false,
           info: false
         }

         const user_ids = Object.keys(data.users);
         console.log(user_ids);
         tableData.clear()
         tableData.rows.add(user_ids.map(user_id => {
            r = [user_id];
            const user  =  data.users[user_id];
            user.forEach(attr => {
               if (attr) {
                  r.push('<i class="fa fa-plus-circle"></i>');
               } else {
                  r.push('<i class="fa fa-minus-circle"></i>');
                }
            });
            console.log(r);
            return r;
         }));
         tableData.draw();
         table.removeClass('hidden');
      }

   });

}