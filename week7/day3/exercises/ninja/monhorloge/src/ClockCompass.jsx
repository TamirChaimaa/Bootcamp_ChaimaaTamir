import React, { Component } from "react";

class ClockCompass extends Component {
  constructor(props) {
    super(props);
    this.state = {
      year: 0,
      month: 0,
      dayOfWeek: 0,
      dayOfMonth: 0,
      hour: 0,
      minute: 0,
      second: 0,
    };
  }

  componentDidMount() {
    this.updateTime();
    this.interval = setInterval(this.updateTime, 1000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  updateTime = () => {
    const now = new Date();
    this.setState({
      year: now.getFullYear(),
      month: now.getMonth(),
      dayOfWeek: now.getDay(),
      dayOfMonth: now.getDate(),
      hour: now.getHours(),
      minute: now.getMinutes(),
      second: now.getSeconds(),
    });
  };

  render() {
    const { year, month, dayOfWeek, dayOfMonth, hour, minute, second } = this.state;

    // Convert month and weekday numbers to names
    const months = [
      "Jan", "Feb", "Mar", "Apr", "May", "Jun",
      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ];
    const weekdays = [
      "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"
    ];

    // Angles for rotation
    const hourAngle = (hour % 12) * 30; // 360/12 = 30deg per hour
    const minuteAngle = minute * 6;     // 360/60 = 6deg per minute
    const secondAngle = second * 6;     // 360/60 = 6deg per second
    const dayOfWeekAngle = dayOfWeek * (360 / 7);
    const dayOfMonthAngle = (dayOfMonth / 31) * 360;
    const monthAngle = (month / 11) * 360;

    const clockStyle = {
      position: "relative",
      width: "300px",
      height: "300px",
      borderRadius: "50%",
      border: "5px solid #333",
      margin: "40px auto",
      fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
      color: "#222",
      backgroundColor: "#f9f9f9",
    };

    const centerStyle = {
      position: "absolute",
      top: "50%",
      left: "50%",
      transform: "translate(-50%, -50%)",
      textAlign: "center",
    };

    // Function to create rotated label styles
    const createRotatedStyle = (angle, position) => {
      // position can be 'top-left', 'bottom-right', etc.
      let baseStyle = {
        position: "absolute",
        transform: `rotate(${angle}deg)`,
        transformOrigin: "center",
        fontWeight: "bold",
        fontSize: "14px",
        userSelect: "none",
      };
      switch (position) {
        case "top-left":
          baseStyle.top = "15px";
          baseStyle.left = "15px";
          break;
        case "bottom-right":
          baseStyle.bottom = "15px";
          baseStyle.right = "15px";
          break;
        case "top-right":
          baseStyle.top = "15px";
          baseStyle.right = "15px";
          break;
        case "bottom-left":
          baseStyle.bottom = "15px";
          baseStyle.left = "15px";
          break;
        case "center-top":
          baseStyle.top = "10%";
          baseStyle.left = "50%";
          baseStyle.transform += " translateX(-50%)";
          break;
        default:
          break;
      }
      return baseStyle;
    };

    return (
      <div style={clockStyle}>
        {/* Year top-left */}
        <div style={createRotatedStyle(0, "top-left")}>
          Year: {year}
        </div>

        {/* Month bottom-right rotated */}
        <div style={createRotatedStyle(monthAngle, "bottom-right")}>
          Month: {months[month]}
        </div>

        {/* Day of week top-right rotated */}
        <div style={createRotatedStyle(dayOfWeekAngle, "top-right")}>
          Day: {weekdays[dayOfWeek]}
        </div>

        {/* Day of month bottom-left rotated */}
        <div style={createRotatedStyle(dayOfMonthAngle, "bottom-left")}>
          Date: {dayOfMonth}
        </div>

        {/* Clock center linear display */}
        <div style={centerStyle}>
          <div style={{ fontSize: "18px", marginBottom: "5px" }}>
            {hour.toString().padStart(2, "0")}:
            {minute.toString().padStart(2, "0")}:
            {second.toString().padStart(2, "0")}
          </div>
          <div>
            {weekdays[dayOfWeek]}, {months[month]} {dayOfMonth}, {year}
          </div>
        </div>

        {/* Optional: analog hands */}
        {/* Hour hand */}
        <div
          style={{
            position: "absolute",
            top: "50%",
            left: "50%",
            width: "6px",
            height: "60px",
            backgroundColor: "#333",
            transformOrigin: "bottom center",
            transform: `translate(-50%, -100%) rotate(${hourAngle + minute / 2}deg)`,
            borderRadius: "3px",
          }}
        ></div>

        {/* Minute hand */}
        <div
          style={{
            position: "absolute",
            top: "50%",
            left: "50%",
            width: "4px",
            height: "90px",
            backgroundColor: "#666",
            transformOrigin: "bottom center",
            transform: `translate(-50%, -100%) rotate(${minuteAngle}deg)`,
            borderRadius: "2px",
          }}
        ></div>

        {/* Second hand */}
        <div
          style={{
            position: "absolute",
            top: "50%",
            left: "50%",
            width: "2px",
            height: "100px",
            backgroundColor: "red",
            transformOrigin: "bottom center",
            transform: `translate(-50%, -100%) rotate(${secondAngle}deg)`,
            borderRadius: "1px",
          }}
        ></div>
      </div>
    );
  }
}

export default ClockCompass;
