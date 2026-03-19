from flask import Flask, render_template, request
import algo 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    input_text = "---------------"
    output_text = "----------------"
    key = "-----"
    algorithm = ""
    operation = ""
    steps = []

    if request.method == "POST":

        algorithm = request.form.get("algorithmType")
        operation = request.form.get("operationType")
        input_text = request.form.get("text").lower()
        key = request.form.get("key")
        
        try:
            
            # Caesar Cipher
            if algorithm == "caesar":
                key = int(key)

                if operation == "encrypt":
                    output_text,steps = algo.ceasor_conversion(input_text, key)

                else:
                    output_text,steps = algo.ceasor_conversion(input_text, -key)

            # Rail Fence Cipher
            elif algorithm == "railfence":
                key = int(key)

                if operation == "encrypt":
                    output_text, steps = algo.railfence_encrypt(input_text, key)

                else:
                    output_text, steps = algo.railfence_decrypt(input_text, key)

            # Vigenere Cipher
            elif algorithm == "vigenere":

                if operation == "encrypt":
                    output_text,steps = algo.vigenere_conversion(input_text, key, 'e')

                else:
                    output_text,steps = algo.vigenere_conversion(input_text, key, 'd')

            # Playfair Cipher
            elif algorithm == "playfair": 

                if operation == "encrypt":
                    output_text, steps = algo.playfair_conversion(input_text, key, 'e')

                else:
                    output_text, steps = algo.playfair_conversion(input_text, key, 'd')

            # Hill Cipher
            elif algorithm == "hill":

                if operation == "encrypt":
                    output_text = algo.hill_encrypt(input_text, key)

                else:
                    output_text = algo.hill_decrypt(input_text, key)

        except Exception as e:
            output_text = "Error: " + str(e)

    return render_template(
        "index.html",
        input_text=input_text,
        output_text=output_text,
        key=key,
        algorithm=algorithm.capitalize(),
        steps=steps,
        )


if __name__ == "__main__":
    app.run(debug=True)