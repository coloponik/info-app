$(document).ready(function () 
{

    $('input[name = "radio"]').click(function () 
    {
        if ($('input[id = "radio_1"]').prop('checked')) 
        {
            $('div[id = "hide"]').show("slow");
            $('input[id = "paymentStep"]').val("");
            $('div[id = "termMonths"]').hide();
            $('div[id = "termDays"]').show();
        }
        if (!$('input[id = "radio_1"]').prop('checked')) 
        {
            $('div[id = "hide"]').hide(300);
            $('input[id = "paymentStep"]').val("1");
            $('div[id = "termDays"]').hide();
            $('div[id = "termMonths"]').show();
        }
    })

    $('#credit').click(function(){
        validateForm();   
    });
    
    function validateForm(){
    
        var amountReg = /\d+([.]\d{1,2})?/
        var rateReg =  /\d+([.]\d{1,2})?/
        var periodReg = /\d+/
        var stepReg = /\d+/

        var notNull = 'Поле не может быть пустым'
        var unsFloat = 'Ожидается положительное число (до 2х знаков после ".") в диапозоне '
        var unsInt = 'Ожидается положительное целочисленное число в диапозоне '
    
        $("#creditAmount").focusin(function() 
        {
            $(this).next(".alert").hide();
        });

        $('#creditAmount').focusout(function()
        {
            if($(this).val() == "")
            {
                $(this).next(".alert").text(notNull).show("fast");
            } 
            else if (!amountReg.test($(this).val()) || ( 20000.00 > $(this).val() ||  $(this).val() > 3000000.00))
            {
                $(this).next(".alert").text(unsFloat + "20 000.00 - 3 000 000.00").show("fast");
            }
        });
    
        $("#creditRate").focusin(function() 
        {
            $(this).next(".alert").hide();
        });

        $('#creditRate').focusout(function()
        {
            if($(this).val() == "")
            {
                $(this).next(".alert").text(notNull).show("fast");
            } 
            else if(!rateReg.test($(this).val()) || ( 0.50 > $(this).val() ||  $(this).val() > 25.00)) 
            {
                $(this).next(".alert").text(unsFloat + "0.50 - 25.00").show("fast");
            }
        });
    
        $("#creditPeriod").focusin(function() 
        {
            $(this).next("div").hide()
        });

        $('#creditPeriod').focusout(function()
        {
            if($(this).val() == "")
            {
                $(this).next(".alert").text(notNull).show("fast");
            } 
            else if(!periodReg.test($(this).val()) || ( 1 > $(this).val() ||  $(this).val() > 90))
            {
                $(this).next(".alert").text(unsInt + "1 - 90").show("fast");
            }
        });

        $("#paymentStep").focusin(function() 
        {
            $(this).next(".alert").hide()
        });

        $('#paymentStep').focusout(function()
        {
            if( $(this).val() == "")
            {
                $(this).next(".alert").text(notNull).show("fast");
            } 
            else if(!stepReg.test( $(this).val()) || ( 1 > $(this).val() ||  $(this).val() > 30))
            {
                $(this).next(".alert").text(unsInt + "1 - 30").show("fast");
            }
            else if($("#creditPeriod").val() % $(this).val() != 0)
            {
                $(this).next(".alert").text("Срок кредита должен быть кратен шагу платежа").show("fast");
            }
        });
    }
});