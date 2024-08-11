# Event-Driven Framework

## Overview

This package provides a flexible event-driven mechanism designed for applications requiring custom event handling. At its core is the EventListener class, which allows you to easily subscribe, unsubscribe, and invoke listeners (callbacks). This class is particularly suited for event-driven architectures such as GUI applications, asynchronous programming, and custom event handling in various types of software.

## Key Features

- Event Subscription: Easily subscribe single or multiple callbacks to events.
- Event Invocation: Trigger all registered listeners with specified arguments.
- Listener Management: Unsubscribe listeners individually or clear all listeners at once.
- Safe Execution: Ensures that all listeners are invoked safely.

## Installation

To install the package, simply run:

```bash
pip install event_listener
```

## Usage

### Basic Example

```python
from event_listener import EventListener

# Create an event listener instance
event = EventListener(name="SampleEvent")

# Define some example callback functions
def on_event_fired(arg1, arg2):
    print(f"Event fired with arguments: {arg1}, {arg2}")

def on_event_fired_again(arg1, arg2):
    print(f"Event fired again with arguments: {arg1}, {arg2}")

# Subscribe the callbacks to the event
event.subscribe(on_event_fired)
event.subscribe(on_event_fired_again)

# Invoke the event with some arguments
event.invoke("Hello", "World")

# Output:
# Event fired with arguments: Hello, World
# Event fired again with arguments: Hello, World

# Clear all listeners
event.clear()

# Or unsubscribe a specific listener
event.unsubscribe(on_event_fired)
```

### Async listener

```python
from event_listener import EventListenerAsync

# Create an event listener instance
event = EventListenerAsync(name="SampleEvent")

# Define some example callback functions
def on_event_fired(arg1, arg2):
    print(f"Event fired with arguments: {arg1}, {arg2}")

def on_event_fired_again(arg1, arg2):
    print(f"Event fired again with arguments: {arg1}, {arg2}")

# Subscribe the callbacks to the event
event.subscribe(on_event_fired)
event.subscribe(on_event_fired_again)

# Invoke will call every method in separate threads.
event.invoke_async("Hello", "World")
```

License
This project is licensed under the MIT License. See the LICENSE file for details.
