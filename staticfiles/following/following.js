$(".followchange").on("submit", function(event) {
    event.preventDefault();
    var form = $(this);
    console.log('form id', form, form.data("id"));
    save_data();


    function save_data() {
      console.log('start AJAX');
      var token = "{{csrf_token}}";
      var profilePk = form.find("input[name='profile_pk']").val();
      console.log(profilePk);
      $.ajax({
        type: "POST",
        headers: { "X-CSRFToken": token },
        url: "{% url 'switch_follow' %}",
        data: {value: profilePk },

        success: function (response) {
          if (response === "removed") {
              form.find(".unfollow-btn").hide();
              form.find(".follow-btn").show();
              $("#error-"+form.data("id")).html(
                  '<p style="color:brown">Unfollowed</p>'
              ).fadeIn().delay(5000).fadeOut();
              }
          else {
              form.find(".follow-btn").hide();
              form.find(".unfollow-btn").show();
              $("#error-"+form.data("id")).html(
                  '<p style="color:green">Followed</p>'
                  ).fadeIn().delay(5000).fadeOut();
              }


          console.log(response);
          console.log(response.responseType)
        },
        error: function (response) {},
      });
    }
  });