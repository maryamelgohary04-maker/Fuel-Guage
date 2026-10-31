# Create an infinite loop that will keep running until we break out of it
# عمل حلقة تكرارية مستمرة لا تتوقف أبداً إلا لو كسرناها بأمر break



    # Try the following block of code, and if an error happens, jump to the 'except' block
    # جرب تنفيذ الأكواد اللي جاية دي، ولو حصل أي خطأ روح فوراً على جزء الـ except



        # Ask the user to type a fraction (like 3/4) and save it in the 'fraction' variable
        # اطلب من المستخدم يكتب كسر (زي 3/4) واحفظ اللي كتبه جوه متغير اسمه fraction




        # Split the fraction string into two parts wherever there is a '/' and store them as numerator (n) and denominator (d)
        # افصل نص الكسر لجزئين عند علامة الشرطة المائلة '/' وخزن الجزء الأول في البسط (n) والثاني في المقام (d)




        # Convert the numerator string 'n' into an integer (whole number)
        # حول شكل البسط النصي 'n' إلى رقم صحيح (integer) عشان نقدر نعمل عليه عمليات حسابية




        # Convert the denominator string 'd' into an integer (whole number)
        # حول شكل المقام النصي 'd' إلى رقم صحيح (integer)



        # Check if the numerator is greater than the denominator, or if the numerator is negative
        # افحص هل البسط أكبر من المقام؟ أو هل البسط رقم بالسالب (أقل من صفر)؟



            # If the fraction is invalid (like 5/4 or -1/2), skip the rest of the loop and ask for input again
            # لو الكسر غلط وغير منطقي (زي 5/4 أو -1/2)، سيب باقي الكود وارجع اعيد اللفة من الأول واطلب إدخال تاني (continue)



        # Calculate the percentage by dividing n by d, multiplying by 100, and rounding to the nearest whole number
        # احسب النسبة المئوية عن طريق قسمة n على d، واضرب الناتج في 100، وقربه لأقرب عدد صحيح




        # Check if the calculated percentage is 1% or less
        # افحص هل النسبة المئوية اللي طلعناها دي 1% أو أقل؟



            # Print the letter 'E' (standing for Empty)
            # اطبع الحرف 'E' (بيرمز لكلمة Empty يعني فاضي)



            # Stop the infinite loop because we got a valid result
            # وقف الحلقة التكرارية تماماً لأننا خلاص وصلنا لنتيجة صحيحة وسليمة (break)



        # Check if the calculated percentage is 99% or more
        # افحص هل النسبة المئوية 99% أو أكتر؟



            # Print the letter 'F' (standing for Full)
            # اطبع الحرف 'F' (بيرمز لكلمة Full يعني ممتلئ)



            # Stop the infinite loop because we got a valid result
            # وقف الحلقة التكرارية خلاص لأننا خلصنا (break)



        # If the percentage is between 2% and 98% (inclusive)
        # لو النسبة المئوية واقعة في النص بين 2% و 98%



            # Print the percentage value followed by a '%' sign
            # اطبع قيمة النسبة المئوية وجنبها علامة في المية '%'



            # Stop the infinite loop because we got a valid result
            # وقف الحلقة التكرارية لأن المهمة تمت بنجاح (break)




    # Catch any errors like typing letters instead of numbers (ValueError) or dividing by zero (ZeroDivisionError)
    # امسك أو التقط أي أخطاء ممكن تحصل، زي إن المستخدم يكتب حروف بدل الأرقام (ValueError) أو إنه يحط المقام بصفر (ZeroDivisionError)



        # Do nothing and just ignore the error, allowing the loop to ask the user for input again
        # متعملش أي حاجة وتجاهل الخطأ بهدوء، عشان تسمح للحلقة إنها تسأل المستخدم يكتب الكسر من جديد وما يحصلش كراش للبرنامج (pass)
        

