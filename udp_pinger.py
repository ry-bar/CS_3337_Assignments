from socket import *
import time

def main():

    logged_statements = True# True or False
    packets_to_send = 10
    dropped_packets = 0
    maximum_rtt = 0
    minimum_rtt = 15# Setting this to something high so that it was always get replaced by the first minimum RTT.
    average_rtt = 0
    to_log_file = []# Things to be written to udp_pinger_logfile.txt


    message = "whats the difference between udp and"# Something to send to the server.



    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.settimeout(1)

    for ping in range(packets_to_send):# Starting to send packets to the server.

        server = 'simplesmtp.thought.net'
        port = 8192


        start_time = time.time()# Starting the timer for RTT
        client_socket.sendto(message.encode(), (server, port))

        try:
            return_message, server = client_socket.recvfrom(1024)# Getting the message back form the server.

            end_time = time.time()# Stopping the timer for RTT

            rtt = end_time - start_time# Getting RTT
            if rtt > maximum_rtt:# Getting the maximum RTT
                maximum_rtt = rtt
            if rtt < minimum_rtt:# Getting the minimum RTT
                minimum_rtt = rtt
            average_rtt += rtt# Keeping to total to get the average at the end.

            if logged_statements:# Storing the things that need to be written to udp_pinger_logfile.txt.
                to_log_file.append(f"Ping {ping+1} RTT:{round((rtt*1000), 3)} ms\nMessage: {return_message.decode()}\n")

        except Exception as e:
            to_log_file.append(f"Ping {ping+1}:{e}\n")# Storing the things that need to be written to udp_pinger_logfile.txt.
            dropped_packets += 1# Keeping track of the dropped packets to compute the final results

    if logged_statements:# Writing everything to udp_pinger_logfile.txt
        with open('udp_pinger_logfile.txt', 'w') as f:
            for log in to_log_file:# Server responses being written first to udp_pinger_logfile.txt.
                f.write(f"{log}\n")
            f.write(f"\n\nMaximum RTT: {round((maximum_rtt * 1000), 3)} ms\n"# Now everything else being written to the file.
                    f"Minimum RTT: {round((minimum_rtt * 1000), 3)} ms\n"
                    f"Average RTT: {round(((average_rtt / (packets_to_send - dropped_packets)) * 1000), 3)} ms\n"
                    f"Packet loss percentage: {round(((dropped_packets / packets_to_send) * 100), 0)}%")











if __name__ == "__main__":
    main()