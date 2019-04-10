from deepdrive_api.client import get_action, Client


def main():
    env = Client(is_remote_client=True, render=True)
    forward = get_action(throttle=1)
    done = False
    while True:
        while not done:
            observation, reward, done, info = env.step(forward)
        print('Episode finished')
        done = env.reset()


if __name__ == '__main__':
    main()
