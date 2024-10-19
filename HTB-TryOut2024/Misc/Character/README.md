# Character
## Description
Security through Induced Boredom is a personal favourite approach of mine. Not as exciting as something like The Fray, but I love making it as tedious as possible to see my secrets, so you can only get one character at a time!
## Approch
i used this script to solve this challange
```python
import subprocess

# Define the command to run nc
command = ['nc', '94.237.49.161', '51290']

# Start the subprocess
process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Initialize an empty string to store the flag
flag = ""

# Initialize the index
index = 0

# Function to send input and get output
def send_input_get_output(input_data):
    process.stdin.write(input_data + '\n')
    process.stdin.flush()
    output = process.stdout.readline()
    return output

# Loop through inputs and get outputs until the output is '}'
while True:
    input_data = str(index)
    output = send_input_get_output(input_data)
    print(f"Input: {input_data} -> Output: {output}")
    
    # Extract the character from the output and append it to the flag
    if "Character at Index" in output:
        char = output.split(": ")[-1].strip()
        flag += char
        if char == '}':
            break
    
    # Increment the index
    index += 1

# Close the process
process.stdin.close()
process.stdout.close()
process.stderr.close()
# process.wait()

# Print the final flag
print(f"The flag is: {flag}")
```
## Flag
```
HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_l0ng!!}
```
