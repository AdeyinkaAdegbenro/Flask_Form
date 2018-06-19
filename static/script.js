function submitFunction (event) {
  event.preventDefault()
  console.log('submitted', event)
  first_name = $('#first_name').val()
  middle_name = $('#middle_name').val()
  last_name = $('#last_name').val()
  date_of_birth = $('#date_of_birth').val()
  address = $('#address').val()
  hobby = $('#hobby').val()
  console.log('values,', first_name, middle_name, last_name, date_of_birth, address, hobby)

  // send  to server
  data = {
    first_name: first_name,
    middle_name: middle_name,
    last_name: last_name,
    date_of_birth: date_of_birth,
    address: address,
    hobby: hobby
  }

  $.ajax({
    type: "POST",
    url: '/submit',
    contentType: 'application/json',
    data: JSON.stringify(data),
    success: function () {
      console.log('data sent to server successfully')
    },
    dataType: 'json'
  });
  
  
  return false
}