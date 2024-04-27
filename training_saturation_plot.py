import pandas as pd

def extract_contents(filename):
    try:
        with open(filename, 'r') as file:
            epoch_list = []
            loss_list = []
            acc_list = []
            for line in file:
                # Find all bracketed content in the current line
                start = 0
                while True:
                    start = line.find('[', start)
                    if start == -1:
                        break
                    end = line.find(']', start)
                    if end == -1:
                        break
                    # process epoch
                    epoch_str = line[start+1:end]
                    epoch_str = epoch_str[5:]
                    epoch_list.append(int(epoch_str))

                    # process loss
                    start = 0
                    start = line.find('Loss: ', start)
                    if start == -1:
                        break
                    end = line.find(', Time: ', start)
                    if end == -1:
                        break
                    loss_str = line[start + 5:end]
                    loss_list.append(float(loss_str))

                    # process loss
                    start = 0
                    start = line.find('Acc: ', start)
                    if start == -1:
                        break
                    end = line.find('%', start)
                    if end == -1:
                        break
                    acc_str = line[start + 4:end]
                    acc_list.append(float(acc_str))
                    start = end + 1
        # Create a DataFrame
        df = pd.DataFrame({
            'epoch': epoch_list,
            'loss': loss_list,
            'acc': acc_list
        })
        df.to_excel("output.xlsx", index=False, engine='openpyxl')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Replace 'example.txt' with the path to your text file
extract_contents('output.txt')
