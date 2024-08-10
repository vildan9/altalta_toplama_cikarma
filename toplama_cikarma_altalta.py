def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems: Problem Sayısı Kontrolü: Fonksiyon ilk olarak problems listesindeki problem sayısının 5'ten fazla olup olmadığını kontrol eder. Eğer fazla ise, 'Error: Too many problems.' mesajını döner.
    if len(problems) > 5:
        return 'Error: Too many problems.'
    #Satır Listeleri: Her bir satır için (üst, orta, alt ve sonuç satırı) boş listeler oluşturulur. Bu listeler her bir problemin parçalarını tutacaktır.
    top_row = []
    middle_row = []
    bottom_row = []
    dashes_row = []
    answers_row = []
    #Problem Ayrıştırma: Her bir problemi boşluk karakterine göre böler (split()). Eğer bir problem 3 parçadan oluşmuyorsa, bu format hatasıdır ve 'Error: Each problem must have two operands and one operator.' mesajını döner.
    for problem in problems:
        # Split each problem into operands and operator
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Each problem must have two operands and one operator.'
        #Operatör Kontrolü: Operatörün sadece + veya - olup olmadığını kontrol eder. Başka bir operatör varsa, 'Error: Operator must be "+" or "-".' mesajını döner.
        #Operand Kontrolü: Operandların sadece rakamlardan oluştuğunu (isdigit()) ve dört rakamı geçmediğini kontrol eder. Geçersizse, 'Error: Numbers must only contain digits.' veya 'Error: Numbers cannot be more than four digits.' mesajlarını döner.

        operand1, operator, operand2 = parts
        
        # Check for valid operator
        if operator not in ('+', '-'):
            return 'Error: Operator must be "+" or "-".'
        
        # Check if operands are digits
        if not (operand1.isdigit() and operand2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        # Check the length of operands
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Calculate width for formatting.
        #Genişlik Hesaplama: Her problemin genişliğini belirler. Genişlik, en uzun operandın uzunluğu artı iki (operatör ve aralarındaki boşluk) olarak hesaplanır.
        # Satır Eklemeleri:
        #Üst satıra, ilk operandı sağa yaslanmış olarak ekler (rjust()).
        #Orta satıra, operatörü ve ikinci operandı ekler (rjust() ile hizalar).
        #Alt satıra, her problem için uygun uzunlukta çizgi karakterleri ekler.

        width = max(len(operand1), len(operand2)) + 2
        top_row.append(operand1.rjust(width))
        middle_row.append(operator + ' ' + operand2.rjust(width - 2))
        bottom_row.append('-' * width)
        
        # Calculate answer if needed
        #Sonuç Hesaplama: Eğer show_answers True ise, operatöre göre toplama veya çıkarma işlemi yapar ve sonucu hesaplar. Sonuçları uygun genişlikte sağa yaslanmış olarak answers_row listesine ekler.
        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            elif operator == '-':
                answer = str(int(operand1) - int(operand2))
            answers_row.append(answer.rjust(width))
    
    # Join each row with four spaces in between
    #Satırları Birleştirme: Her bir satır, dört boşluk ile ayrılarak birleştirilir. Eğer show_answers True ise, sonuç satırı da eklenir.
    #Sonuç Dönme: Düzenlenmiş problemler döndürülür.
    
    arranged_problems = '    '.join(top_row) + '\n' + \
                        '    '.join(middle_row) + '\n' + \
                        '    '.join(bottom_row)
    
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers_row)
    
    return arranged_problems

# Example usage:
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
# Expected Output: "Error: Operator must be '+' or '-'."
