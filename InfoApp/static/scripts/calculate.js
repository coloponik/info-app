$(document).ready(function ()
{
    $('input[name = "rate"]').click(function ()
    {
        if ($('input[id = "rateDay"]').prop('checked'))
        {
            $('div[id = "hide"]').show("slow");
            // $('input[id = "payStep"]').val("");
            $('div[id = "termMonths"]').hide();
            $('div[id = "termDays"]').show();
        }
        if (!$('input[id = "rateDay"]').prop('checked'))
        {
            $('div[id = "hide"]').hide(300);
            // $('input[id = "payStep"]').val("1");
            $('div[id = "termDays"]').hide();
            $('div[id = "termMonths"]').show();
        }
    })
});